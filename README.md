Bill Splitter
=============

Demo: http://home.nicolasbouliane.com/billsplitter

A simple shared expense manager for Django. Useful for couples and roommates looking to fairly split their expenses.

The project is an early fork of [Groupshex](https://github.com/lracicot/groupshex). It has a simpler model and notably omits to account for people who join the group later.

How it works
------------

Alice and Bob live together. They write their expenses in Bill Splitter. At any moment, they can see how much 
they've each spent. if Bob has spent less for shared expenses, he can take care the next few bills to make it fair for Alice.

Since it's all written down, there's no need to stick bills on the fridge, remember who bought what and guess who pays
rent next.

Why it's awesome
----------------

* **It's simple.** It has already passed the girlfriend test with flying colors. It's much easier to fairly track expenses.
* **It's mobile.** The interface is made from the ground up to work great on mobile devices.
* **It's extensible.** The models are simple and the views are class-based. Extending it should be a no-brainer.

What's missing
--------------

I consider the app feature-complete for my own needs, but I plan progressively add new features, including iOS icons.

Bill Splitter notably fails to account for people who join the group at a later time. I do not plan to add this feature yet.
