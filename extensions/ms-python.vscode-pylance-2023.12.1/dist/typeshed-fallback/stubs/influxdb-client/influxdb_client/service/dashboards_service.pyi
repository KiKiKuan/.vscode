from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class DashboardsService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def delete_dashboards_id(self, dashboard_id, **kwargs): ...
    def delete_dashboards_id_with_http_info(self, dashboard_id, **kwargs): ...
    async def delete_dashboards_id_async(self, dashboard_id, **kwargs): ...
    def delete_dashboards_id_cells_id(self, dashboard_id, cell_id, **kwargs): ...
    def delete_dashboards_id_cells_id_with_http_info(self, dashboard_id, cell_id, **kwargs): ...
    async def delete_dashboards_id_cells_id_async(self, dashboard_id, cell_id, **kwargs): ...
    def delete_dashboards_id_labels_id(self, dashboard_id, label_id, **kwargs): ...
    def delete_dashboards_id_labels_id_with_http_info(self, dashboard_id, label_id, **kwargs): ...
    async def delete_dashboards_id_labels_id_async(self, dashboard_id, label_id, **kwargs): ...
    def delete_dashboards_id_members_id(self, user_id, dashboard_id, **kwargs): ...
    def delete_dashboards_id_members_id_with_http_info(self, user_id, dashboard_id, **kwargs): ...
    async def delete_dashboards_id_members_id_async(self, user_id, dashboard_id, **kwargs): ...
    def delete_dashboards_id_owners_id(self, user_id, dashboard_id, **kwargs): ...
    def delete_dashboards_id_owners_id_with_http_info(self, user_id, dashboard_id, **kwargs): ...
    async def delete_dashboards_id_owners_id_async(self, user_id, dashboard_id, **kwargs): ...
    def get_dashboards(self, **kwargs): ...
    def get_dashboards_with_http_info(self, **kwargs): ...
    async def get_dashboards_async(self, **kwargs): ...
    def get_dashboards_id(self, dashboard_id, **kwargs): ...
    def get_dashboards_id_with_http_info(self, dashboard_id, **kwargs): ...
    async def get_dashboards_id_async(self, dashboard_id, **kwargs): ...
    def get_dashboards_id_cells_id_view(self, dashboard_id, cell_id, **kwargs): ...
    def get_dashboards_id_cells_id_view_with_http_info(self, dashboard_id, cell_id, **kwargs): ...
    async def get_dashboards_id_cells_id_view_async(self, dashboard_id, cell_id, **kwargs): ...
    def get_dashboards_id_labels(self, dashboard_id, **kwargs): ...
    def get_dashboards_id_labels_with_http_info(self, dashboard_id, **kwargs): ...
    async def get_dashboards_id_labels_async(self, dashboard_id, **kwargs): ...
    def get_dashboards_id_members(self, dashboard_id, **kwargs): ...
    def get_dashboards_id_members_with_http_info(self, dashboard_id, **kwargs): ...
    async def get_dashboards_id_members_async(self, dashboard_id, **kwargs): ...
    def get_dashboards_id_owners(self, dashboard_id, **kwargs): ...
    def get_dashboards_id_owners_with_http_info(self, dashboard_id, **kwargs): ...
    async def get_dashboards_id_owners_async(self, dashboard_id, **kwargs): ...
    def patch_dashboards_id(self, dashboard_id, **kwargs): ...
    def patch_dashboards_id_with_http_info(self, dashboard_id, **kwargs): ...
    async def patch_dashboards_id_async(self, dashboard_id, **kwargs): ...
    def patch_dashboards_id_cells_id(self, dashboard_id, cell_id, cell_update, **kwargs): ...
    def patch_dashboards_id_cells_id_with_http_info(self, dashboard_id, cell_id, cell_update, **kwargs): ...
    async def patch_dashboards_id_cells_id_async(self, dashboard_id, cell_id, cell_update, **kwargs): ...
    def patch_dashboards_id_cells_id_view(self, dashboard_id, cell_id, view, **kwargs): ...
    def patch_dashboards_id_cells_id_view_with_http_info(self, dashboard_id, cell_id, view, **kwargs): ...
    async def patch_dashboards_id_cells_id_view_async(self, dashboard_id, cell_id, view, **kwargs): ...
    def post_dashboards(self, create_dashboard_request, **kwargs): ...
    def post_dashboards_with_http_info(self, create_dashboard_request, **kwargs): ...
    async def post_dashboards_async(self, create_dashboard_request, **kwargs): ...
    def post_dashboards_id_cells(self, dashboard_id, create_cell, **kwargs): ...
    def post_dashboards_id_cells_with_http_info(self, dashboard_id, create_cell, **kwargs): ...
    async def post_dashboards_id_cells_async(self, dashboard_id, create_cell, **kwargs): ...
    def post_dashboards_id_labels(self, dashboard_id, label_mapping, **kwargs): ...
    def post_dashboards_id_labels_with_http_info(self, dashboard_id, label_mapping, **kwargs): ...
    async def post_dashboards_id_labels_async(self, dashboard_id, label_mapping, **kwargs): ...
    def post_dashboards_id_members(self, dashboard_id, add_resource_member_request_body, **kwargs): ...
    def post_dashboards_id_members_with_http_info(self, dashboard_id, add_resource_member_request_body, **kwargs): ...
    async def post_dashboards_id_members_async(self, dashboard_id, add_resource_member_request_body, **kwargs): ...
    def post_dashboards_id_owners(self, dashboard_id, add_resource_member_request_body, **kwargs): ...
    def post_dashboards_id_owners_with_http_info(self, dashboard_id, add_resource_member_request_body, **kwargs): ...
    async def post_dashboards_id_owners_async(self, dashboard_id, add_resource_member_request_body, **kwargs): ...
    def put_dashboards_id_cells(self, dashboard_id, cell, **kwargs): ...
    def put_dashboards_id_cells_with_http_info(self, dashboard_id, cell, **kwargs): ...
    async def put_dashboards_id_cells_async(self, dashboard_id, cell, **kwargs): ...
