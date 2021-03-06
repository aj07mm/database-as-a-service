# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from functools import wraps
from django.test import TestCase


def skip_unless_not_abstract(method):
    @wraps(method)
    def deco(*args, **kwargs):
        class_name = args[0].__class__.__name__
        if class_name.startswith('Abstract'):
            print("{!r} is abstract!".format(class_name))
            return lambda x, y: x
        return method(*args, **kwargs)
    return deco


class AbstractReplicationTopologySettingsTestCase(TestCase):

    def setUp(self):
        self.replication_topology = self._get_replication_topology_driver()

    def _get_replication_topology_driver(self):
        return None

    def _get_deploy_settings(self):
        raise NotImplementedError

    def _get_clone_settings(self):
        raise NotImplementedError

    def _get_resize_settings(self):
        raise NotImplementedError

    def _get_restore_snapshot_settings(self):
        return (
            'workflow.steps.util.restore_snapshot.restore_snapshot.RestoreSnapshot',
            'workflow.steps.util.restore_snapshot.grant_nfs_access.GrantNFSAccess',
            'workflow.steps.util.restore_snapshot.stop_database.StopDatabase',
            'workflow.steps.util.restore_snapshot.umount_data_volume.UmountDataVolume',
            'workflow.steps.util.restore_snapshot.update_fstab.UpdateFstab',
            'workflow.steps.util.restore_snapshot.mount_data_volume.MountDataVolume',
            'workflow.steps.util.restore_snapshot.start_database.StartDatabase',
            'workflow.steps.util.restore_snapshot.make_export_snapshot.MakeExportSnapshot',
            'workflow.steps.util.restore_snapshot.update_dbaas_metadata.UpdateDbaaSMetadata',
            'workflow.steps.util.restore_snapshot.clean_old_volumes.CleanOldVolumes',
        )

    def _get_get_volume_migration_settings(self):
        return (
            'workflow.steps.util.volume_migration.create_volume.CreateVolume',
            'workflow.steps.util.volume_migration.mount_volume.MountVolume',
            'workflow.steps.util.volume_migration.stop_database.StopDatabase',
            'workflow.steps.util.volume_migration.copy_data.CopyData',
            'workflow.steps.util.volume_migration.umount_volumes.UmountVolumes',
            'workflow.steps.util.volume_migration.update_fstab.UpdateFstab',
            'workflow.steps.util.volume_migration.start_database.StartDatabase',
            'workflow.steps.util.volume_migration.update_dbaas_metadata.UpdateDbaaSMetadata',
        )

    @skip_unless_not_abstract
    def test_deploy_settings(self):
        self.assertEqual(
            self._get_deploy_settings(),
            self.replication_topology.get_deploy_steps()
        )

    @skip_unless_not_abstract
    def test_clone_settings(self):
        self.assertEqual(
            self._get_clone_settings(),
            self.replication_topology.get_clone_steps()
        )

    @skip_unless_not_abstract
    def test_resize_steps(self):
        self.assertEqual(
            self._get_resize_settings(),
            self.replication_topology.get_resize_steps()
        )

    @skip_unless_not_abstract
    def test_restore_snapshot_steps(self):
        self.assertEqual(
            self._get_restore_snapshot_settings(),
            self.replication_topology.get_restore_snapshot_steps()
        )

    @skip_unless_not_abstract
    def test_resize_stepsvolume_migration_steps(self):
        self.assertEqual(
            self._get_get_volume_migration_settings(),
            self.replication_topology.get_volume_migration_steps()
        )
