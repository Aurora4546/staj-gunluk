from odoo import _, exceptions


def activate_card(card_id):
    card_id.write({'active': True,
                   'state': 'assigned_to_user'})


def deactivate_card(card_id, reason=''):
    # we ll manage the state management in unlink
    if reason == 'no_movement':
        for c in card_id:
            c.env.get('deactivate.no.moving.cards.activity').action_create_activity(c)
    card_id.unlink(reason=reason)


def deactivate_card_auths(card_id):
    if card_id.auth_id:
        # card_id.auth_id.active = False
        card_id.auth_id.unlink()


def copy_card_auths(self, new_card_id, old_card_id, active_auth_ids=False):
    if active_auth_ids:
        for a in active_auth_ids:
            a.write({'card_id': new_card_id.id, 'active': True}, pass_sync=False)
    # old_card_id.auth_id = False
    # card_auth_obj = self.env['hr.attendance.card.authorization']
    #
    # if active_auth_ids:
    #     card_auths = card_auth_obj.search(
    #         [('card_id', '=', old_card_id.id), ('active', '=', False), ('id', 'in', active_auth_ids)])
    # else:
    #     card_auths = card_auth_obj.search(
    #         [('card_id', '=', old_card_id.id), ('active', '=', False)], order='id desc', limit=1)
    # deactivate_card_auths(new_card_id)
    # for auth in card_auths:
    #     new_card_id.auth_id += auth.copy(default={'card_id': new_card_id.id, 'active': True})


def check_card_no(obj, check_field):
    f = getattr(obj, check_field)
    if f and len(f) < 8:
        setattr(obj, check_field, False)
        return {'warning': {'title': _("Kart No Hatası"),
                            'message': _("Okutulan Kart No 8 karakter olmalıdır.")}}

    emp_id = hasattr(obj, 'employee_id') and getattr(obj, 'employee_id')

    if emp_id and f == str(emp_id.personel_id):
        setattr(obj, check_field, False)
        return {'warning': {'title': _("Kart No Hatası"),
                            'message': _("Kart No yerine Sicil No Girdiniz.")}}

    return False


def control_card_owner(card_id, employee_id=False):
    # passive cards can be used over and over.
    will_raise = False
    # print(card_id.employee_id, card_id.env.ref("hr_attendance_ext.hr_employee_authorization_temp"))
    if card_id.active and card_id.employee_id and card_id.employee_id != card_id.env.ref(
            "hr_attendance_ext.hr_employee_authorization_temp"):
        if employee_id:
            if card_id.employee_id.id != employee_id.id:
                will_raise = True
        else:
            will_raise = True

    if will_raise:
        raise exceptions.ValidationError(
            _("Card already in use by: {}-{}").format(card_id.employee_id.personel_id,
                                                      card_id.employee_id.name))
    return False
