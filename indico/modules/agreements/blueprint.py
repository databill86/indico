# This file is part of Indico.
# Copyright (C) 2002 - 2015 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from indico.web.flask.wrappers import IndicoBlueprint

from indico.modules.agreements.controllers import (RHAgreementForm, RHAgreementManager, RHAgreementManagerDetails,
                                                   RHAgreementManagerDetailsSendAll, RHAgreementManagerDetailsRemindAll)

agreements_blueprint = _bp = IndicoBlueprint('agreements', __name__, template_folder='templates')


# Event management
_bp.add_url_rule('/event/<confId>/manage/agreements/', 'event_agreements', RHAgreementManager)
_bp.add_url_rule('/event/<confId>/manage/agreements/<definition>',
                 'event_agreements_details', RHAgreementManagerDetails)
_bp.add_url_rule('/event/<confId>/manage/agreements/<definition>/send_all',
                 'event_agreements_details_send_all', RHAgreementManagerDetailsSendAll)
_bp.add_url_rule('/event/<confId>/manage/agreements/<definition>/remind_all',
                 'event_agreements_details_remind_all', RHAgreementManagerDetailsRemindAll)

# Event
_bp.add_url_rule('/event/<confId>/agreement/<int:id>-<uuid>',
                 'agreement_form', RHAgreementForm, methods=('GET', 'POST'))
