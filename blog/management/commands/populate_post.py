from typing import Any
from blog.models import Post ,Category

from django.core.management.base import BaseCommand
 
import random
class Command(BaseCommand):
    help = "This command inserts post data"
    
    def handle(self, *args: Any, **options: Any):
        # Delete exiting data 
        Post.objects.all().delete()
        # Your code for inserting post data follows...

        titles=[
            "Employee Information",
            "Product Inventory",
            "Sales Report",
            "Customer Feedback",
            "Financial Transactions",
            "Student Grades",
            "Project Milestones",
            "Website Analytics",
            "Stock Market Data",
            "Medical Records",
            "Library Catalog",
            "Event Registrations",
            "Survey Responses",
            "Social Media Engagement",
            "Employee Training Records",
            "Shipping and Delivery Status",
            "Hotel Room Reservations",
            "Vehicle Maintenance Logs",
            "Weather Forecast",
            "Real Estate Listings"
        ]

        contents = [
            "An ordered sequence of elements, commonly used for storing data in programming.",
            "A linear data structure containing a collection of elements accessed by their index.",
            "A versatile tool for organizing and managing data efficiently in computer science.",
            "A fundamental building block in many programming languages, offering fast access to elements.",
            "A compact and efficient means of storing homogeneous data types in contiguous memory locations.",
            "A powerful tool for representing lists, matrices, and other structured data in computer programs.",
            "A foundational concept in algorithm design, enabling efficient manipulation and processing of data.",
            "A cornerstone of modern software development, facilitating the implementation of various algorithms and data structures.",
            "A staple of computer science, providing a flexible and scalable approach to data storage and retrieval.",
            "A go-to solution for tasks ranging from simple list management to complex numerical computations.",
            "A critical component in the implementation of data structures like stacks, queues, and hash tables.",
            "An essential tool for handling large datasets and streamlining computational tasks.",
            "A commonly used abstraction for representing collections of objects or values in software engineering.",
            "A key element in the implementation of dynamic programming algorithms and algorithms with time complexity analysis.",
            "A foundational concept in computer programming, offering a straightforward means of organizing and manipulating data.",
            "A ubiquitous feature of programming languages, offering developers a flexible means of data representation.",
            "A core concept in computer science education, teaching students fundamental principles of data storage and manipulation.",
            "A versatile tool for solving a wide range of computational problems, from sorting and searching to graph traversal.",
            "A critical component in the development of efficient and scalable software solutions across various domains.",
            "A fundamental concept in computer programming, empowering developers to solve complex problems with elegance and efficiency."
        ]

        img_urls=[
            'https://picsum.photos/id/1/800/400',
            'https://picsum.photos/id/2/800/400',
            'https://picsum.photos/id/3/800/400',
            'https://picsum.photos/id/4/800/400',
            'https://picsum.photos/id/5/800/400',
            'https://picsum.photos/id/6/800/400',
            'https://picsum.photos/id/7/800/400',
            'https://picsum.photos/id/8/800/400',
            'https://picsum.photos/id/9/800/400',
            'https://picsum.photos/id/10/800/400',
            'https://picsum.photos/id/11/800/400',
            'https://picsum.photos/id/12/800/400',
            'https://picsum.photos/id/13/800/400',
            'https://picsum.photos/id/14/800/400',
            'https://picsum.photos/id/15/800/400',
            'https://picsum.photos/id/16/800/400',
            'https://picsum.photos/id/17/800/400',
            'https://picsum.photos/id/18/800/400',
            'https://picsum.photos/id/19/800/400',
            'https://picsum.photos/id/20/800/400',
        ]
        categories=Category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls):
            category=random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))