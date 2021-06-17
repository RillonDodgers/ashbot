"""MigrationForQuotesTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForQuotesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("quotes") as table:
            table.increments("id")
            table.string("quote")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("quotes")
