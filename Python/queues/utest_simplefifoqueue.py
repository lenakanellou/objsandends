import unittest
from simplefifoqueue import simpleFifoQueue, ERROR, SUCCESS
from io import StringIO
import sys

class TestSimpleFifoQueue(unittest.TestCase):
    
    def setUp(self):
        """Create a simpleFifoQueue instance for testing."""
        self.queue = simpleFifoQueue(capacity=3)

    def test_enqueue(self):
        print("Testing the enqueue method...")
        """Test various scenarios for enqueueing elements."""
        test_cases = [
            (10, SUCCESS),
            (20, SUCCESS),
            (30, SUCCESS),
            (40, ERROR)  # Expect ERROR because the queue is full
        ]
        
        for data, expected in test_cases:
            with self.subTest(data=data):
                self.assertEqual(self.queue.simpleEnqueue(data), expected)

    def test_dequeue(self):
        print("Testing the dequeue method...")
        """Test dequeueing elements and handling an empty queue."""
        self.queue.simpleEnqueue(10)
        self.queue.simpleEnqueue(20)

        expected_dequeues = [10, 20, None]  # Expecting None after dequeuing all
        actual_dequeues = []
        
        for _ in range(3):  # Attempt to dequeue three times
            actual_dequeues.append(self.queue.simpleDequeue())
        
        self.assertEqual(actual_dequeues, expected_dequeues)

    def test_peek(self):
        print("Testing the peek method...")
        """Test peeking at the head element and handling an empty queue."""
        self.queue.simpleEnqueue(10)
        self.queue.simpleEnqueue(20)
        
        # Peek should return the first element
        self.assertEqual(self.queue.simpleQueuePeek(), 10)  # Should peek at 10

        self.queue.simpleDequeue()  # Remove 10
        self.assertEqual(self.queue.simpleQueuePeek(), 20)  # Now peek at 20

        self.queue.simpleDequeue()  # Remove 20
        self.assertIsNone(self.queue.simpleQueuePeek())  # Should return None

    def test_display(self):
        print("Testing the display method...")
        """Test the display function for various queue states."""
        self.queue.simpleEnqueue(10)
        self.queue.simpleEnqueue(20)

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.queue.simpleQueueDisplay()  # Call the display method
        
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check the captured output
        output = captured_output.getvalue()
        
        # Assert that the output contains expected strings
        self.assertIn("10  <--", output)  # Check for first item
        self.assertIn("20  <--", output)  # Check for second item
        self.assertIn("Total elements: 2", output)  # Check for total elements

        # Test display for an empty queue
        self.queue.simpleDequeue()  # Remove the first element
        self.queue.simpleDequeue()  # Remove the second element
        
        # Redirect stdout again
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.queue.simpleQueueDisplay()  # Call display for empty queue
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Check output for empty queue
        output = captured_output.getvalue()
        self.assertIn("Queue is empty.", output)  # Ensure the empty message is displayed


    def test_edge_cases(self):
        """Test various edge cases of the queue."""
        self.assertIsNone(self.queue.simpleDequeue())  # Empty queue
        self.assertIsNone(self.queue.simpleQueuePeek())  # Peek empty queue
        self.assertEqual(self.queue.simpleEnqueue(None), SUCCESS)  # Enqueue None
        self.assertEqual(self.queue.simpleDequeue(), None)  # Dequeue None

if __name__ == '__main__':
    unittest.main()

