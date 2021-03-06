# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.contrib.auth.models import User, Group

from ..models import Team, Role, AccountUser

from .user import CustomUserAdmin
from .role import RoleAdmin
from .team import TeamAdmin

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(AccountUser, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Team, TeamAdmin)
