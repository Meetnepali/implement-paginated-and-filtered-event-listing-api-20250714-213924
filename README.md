# Guidance for Task

## Task Overview
You are provided with a partially implemented FastAPI backend for a library management system. The existing code includes basic schemas, routers, and in-memory data storage, but is incomplete: some integrations and error handling need attention, and features such as authorization, validation, and error handling must be verified and enhanced.

### Key Requirements
- **User Registration**: Implement secure user registration with Pydantic validation, including custom constraints and error handling for duplicate users.
- **Book Reservation**: Only registered users (with proper dependency-based authorization) can reserve a book. Validate all input and ensure business rules (e.g., a user can reserve a book only once, book must exist).
- **Routers/Modules**: Use FastAPI routers for separation of user and reservation endpoints.
- **Pydantic Models**: Use models for all requests/responses and add custom validators as needed.
- **Authorization**: Authorization depends on a special header (see the dependencies file) and must ensure only registered users can act.
- **Async Handlers**: All endpoints should be fully async.
- **Error Handling**: Provide consistent JSON error responses for all error types using centralized exception handlers. Ensure all handlers and exceptions use correct HTTP status codes and format.

## Verifying Your Solution
- Confirm all endpoints correctly validate input and reject invalid or duplicate data with standardized error JSON.
- Ensure business rules (user existence, book existence, single reservation per user/book) are checked and enforced.
- Ensure only registered users can reserve books and that authorization is enforced via dependency injection for reservations.
- Verify that all route handlers are fully async and use the simulated async data functions.
- Check that all errors (validation, business, unexpected) are consistently handled by the centralized error system.
- All endpoints must return correct HTTP status codes and JSON error format (not default/exposing stack traces).

## Notes
- The current setup uses an in-memory DB (Python dict), so there's no persistence after process restart.
- Only modify/add code within the provided file structure and do not introduce extra files or database engines.
- Do not provide environment or run instructions in the README.
