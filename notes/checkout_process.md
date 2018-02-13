# Checkout Process

1. Cart -> Checkout view
	?

	- Login or Enter an email (as guest)
	- Shipping Address
	- Billing info
		- Billing Address
		- Payment / Card

2. Billing App/Component
	- Billing Profile
		- Associated with a User or Email (guest email)
		- generate payment processor or token(Stripe or Braintree)

3. Orders / Invoices Component
	- Connection the Billing profile
	- shipping / billing address
	- status -- Shipped? Cancelled?