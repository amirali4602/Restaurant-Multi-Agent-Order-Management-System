# Sprint 6 – Chef Agent Workflow

## Goal

Extend the multi-agent communication by introducing the ChefAgent.

## Completed

- Added ChefAgent
- Added PREPARE_ORDER performative
- Added ORDER_READY performative
- Implemented simulated cooking process
- Extended OrderAgent orchestration

## Workflow

OrderAgent

↓

CHECK_INVENTORY

↓

InventoryAgent

↓

INVENTORY_OK

↓

OrderAgent

↓

PREPARE_ORDER

↓

ChefAgent

↓

ORDER_READY

↓

OrderAgent

## Result

Three SPADE agents successfully communicate through an XMPP server using asynchronous behaviours.