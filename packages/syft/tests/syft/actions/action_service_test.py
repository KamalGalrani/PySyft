# stdlib

# third party

# syft absolute
from syft.core.node.new.action_object import ActionObject
from syft.core.node.new.context import AuthedServiceContext


def get_auth_ctx(worker):
    return AuthedServiceContext(node=worker, credentials=worker.signing_key.verify_key)


def test_action_service_sanity(worker):
    service = worker.get_service("actionservice")

    obj = ActionObject.from_obj("abc").ok()

    pointer = service.set(get_auth_ctx(worker), obj).ok()

    assert len(service.store.data) == 1
    res = pointer.capitalize()
    assert res[0] == "A"