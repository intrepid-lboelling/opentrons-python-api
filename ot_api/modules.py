#!/usr/bin/env python

from typing import Optional
from ot_api.decorators import command, request_with_run_id
import ot_api.requestor
import ot_api.runs


def list_connected_modules():
    """List the connected modules"""
    return ot_api.requestor.get('/modules')['data']


@command
def open_labware_latch(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {"moduleId": module_id}
    return ot_api.runs.enqueue_command(
        "heaterShaker/openLabwareLatch",
        params,
        intent="setup",
        run_id=run_id,
    )


@command
def close_labware_latch(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {"moduleId": module_id}
    return ot_api.runs.enqueue_command(
        "heaterShaker/closeLabwareLatch",
        params,
        intent="setup",
        run_id=run_id,
    )


@command
def wait_for_temperature(
    module_id: str,
    temp: float,  # target temp in deg C
    run_id: Optional[str] = None,
):
    params = {
        "moduleId": module_id,
        "celsius": temp,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/waitForTemperature", params, intent="setup", run_id=run_id
    )


@command
def set_target_temperature(
    module_id: str,
    temp: float,  # target temp in deg C
    run_id: Optional[str] = None,
):
    params = {
        "moduleId": module_id,
        "celsius": temp,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/setTargetTemperature", params, intent="setup", run_id=run_id
    )


@command
def deactivate_heater(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {
        "moduleId": module_id,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/deactivateHeater", params, intent="setup", run_id=run_id
    )


@command
def set_wait_shake_speed(
    module_id: str,
    rpm: float,  # target speed in rotations per minute
    run_id: Optional[str] = None,
):
    assert 200.0 <= rpm <= 3000.0
    params = {
        "moduleId": module_id,
        "rpm": rpm,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/setAndWaitForShakeSpeed",
        params,
        intent="setup",
        run_id=run_id,
    )


@command
def deactivate_shaker(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {"moduleId": module_id}
    return ot_api.runs.enqueue_command(
        "heaterShaker/deactivateShaker",
        params,
        intent="setup",
        run_id=run_id,
    )


@command
def load_module(slot: int, model: str, module_id: str, run_id: str = None):
    """ Load a module into a slot """
    assert slot in range(1, 13)
    return ot_api.runs.enqueue_command("loadModule",
        params={"location": {
            "slotName": str(slot),
        },
        "model": model,
        "moduleId": module_id,
        }, intent="setup", run_id=run_id)

@command
def load_adapter(load_name:str, namespace: str, version: int, module_id: str, run_id: str = None, labware_id=None, display_name=None):
  """ Add a labware to a slot """
  # if type(slot) == int:
  #   assert slot in range(1, 13)

  data = {
    "location": {
        "moduleId": module_id
    },
    "loadName": load_name,
    "namespace": namespace,
    "version": version,
    "labwareId": labware_id,
    "displayName": display_name,
  }
  return ot_api.runs.enqueue_command("loadLabware", data, intent="setup", run_id=run_id)

@command
def temperature_module_set_temperature(celsius: float, module_id: str, run_id: str = None):
    """ Set the temperature of a temperature module """
    return ot_api.runs.enqueue_command("temperatureModule/setTargetTemperature",
        {"celsius": celsius, "moduleId": module_id},
        intent="setup", run_id=run_id)


@command
def temperature_module_deactivate(module_id: str, run_id: str = None):
    """ Deactivate a temperature module """
    return ot_api.runs.enqueue_command("temperatureModule/deactivate",
        {"moduleId": module_id}, intent="setup", run_id=run_id)
