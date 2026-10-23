from collections import deque
import time


class CoffeeShopQueue:

  def __init__(self):
    # Initialize an empty queue for orders
    self.order_queue = deque()

  def add_order(self, customer_name, coffee_type):
    """Add a new customer order to the back of the queue."""
    order = {"customer": customer_name, "coffee": coffee_type}
    self.order_queue.append(order)
    print(f"\n[Order Received] {customer_name}'s {coffee_type} added to queue.")

  def process_order(self):
    """Process (serve) the order at the front of the queue."""
    if not self.order_queue:
      print("\n[Queue Empty] No pending coffee orders to process!")
      return

    # popleft() removes the first element (FIFO behavior)
    order = self.order_queue.popleft()
    print(f"\n[Brewing...] Preparing {order['coffee']} for {order['customer']}...")
    time.sleep(1)  # Simulate preparation time
    print(
        f"[Ready!] {order['coffee']} for {order['customer']} is ready for"
        " pickup! ☕"
    )

  def view_queue(self):
    """Display all pending orders currently in line."""
    if not self.order_queue:
      print("\n[Queue Status] The coffee queue is currently empty.")
      return

    print("\n--- Current Coffee Order Queue ---")
    for index, order in enumerate(self.order_queue, start=1):
      print(f"{index}. {order['customer']} -> {order['coffee']}")
    print("----------------------------------")


def main():
  shop = CoffeeShopQueue()

  while True:
    print("\n=== ☕ Python Bean Coffee Shop ===")
    print("1. Place an Order")
    print("2. Process Next Order (Barista)")
    print("3. View Current Queue")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
      name = input("Enter customer name: ").strip()
      coffee = input(
          "Enter coffee type (e.g., Iced Latte, Espresso, Cappuccino): "
      ).strip()
      if name and coffee:
        shop.add_order(name, coffee)
      else:
        print("⚠️ Customer name and coffee type cannot be empty.")

    elif choice == "2":
      shop.process_order()

    elif choice == "3":
      shop.view_queue()

    elif choice == "4":
      print(
          "Thanks for running the coffee shop! Closing for the day. Goodbye! 👋"
      )
      break
    else:
      print("⚠️ Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
  main()