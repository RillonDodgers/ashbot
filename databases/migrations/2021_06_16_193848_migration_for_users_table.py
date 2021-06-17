"""MigrationForUsersTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("guilds") as table:
            table.increments("id")
            table.integer("guild_number")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("guilds")
