//To understand this binding, we have to understand the call-site: the location in code where a function
// is called (not where it's declared). We must inspect the call-site to answer the question: what's this
// this a reference to?


// the call-site to see how foo() is called. In our snippet, foo() is called with a plain, un-decorated function reference.
//  None of the other rules we will demonstrate will apply here, so the default binding applies instead.
//default binding 
function foo() {
	console.log( this.a );
}

var a = 2;

foo(); // 2





function foo() {
	"use strict";

	console.log( this.a );
}

var a = 2;

foo(); // TypeError: `this` is `undefined`




// the call-site uses the obj context to reference the function, so you could say that
//  the obj object "owns" or "contains" the function reference at the time the function is called.
//implicit binding 

function foo() {
	console.log( this.a );
}

var obj = {
	a: 2,
	foo: foo
};

obj.foo(); // 2

//top last level will be considered

function foo() {
	console.log( this.a );
}

var obj2 = {
	a: 42,
	foo: foo
};

var obj1 = {
	a: 2,
	obj2: obj2
};

obj1.obj2.foo(); // 42

//explicit binding

function foo() {
	console.log( this.a );
}

var obj = {
	a: 2
};

foo.call( obj ); // 2


//hard binding
function foo() {
	console.log( this.a );
}

var obj = {
	a: 2
};

var bar = function() {
	foo.call( obj );
};

bar(); // 2
setTimeout( bar, 100 ); // 2

// `bar` hard binds `foo`'s `this` to `obj`
// so that it cannot be overriden
bar.call( window ); // 2







//bind
function foo(something) {
	console.log( this.a, something );
	return this.a + something;
}

var obj = {
	a: 2
};

var bar = foo.bind( obj );

var b = bar( 3 ); // 2 3
console.log( b ); // 5




//precedence 
function foo() {
	console.log( this.a );
}

var obj1 = {
	a: 2,
	foo: foo
};

var obj2 = {
	a: 3,
	foo: foo
};

obj1.foo(); // 2
obj2.foo(); // 3

obj1.foo.call( obj2 ); // 3
obj2.foo.call( obj1 ); // 2

//explicit wins






// Is the function called with call or apply (explicit binding), even hidden inside a bind
//  hard binding? If so, this is the explicitly specified object.

// var bar = foo.call( obj2 )

// Is the function called with a context (implicit binding), otherwise known as an
//  owning or containing object? If so, this is that context object.

// var bar = obj1.foo()

// Otherwise, default the this (default binding). If in strict mode, pick undefined,
//  otherwise pick the global object.

// var bar = foo()

// If the functions in question don't care about this, you need a
//  placeholder value, and null might seem like a reasonable choice as shown in this snippet.

//lexical this

// benefit of using arrow functions
//  is that it reduces the confusion surrounding the this keyword. In code with multiple nested functions,
//   it can be difficult to keep track of and remember to bind the correct this context. 
//   In ES5, you can use workarounds like the .bind method 98or creating a closure using var self = this;.

// Because arrow functions allow you to retain the scope of the caller inside the function, 
// you don’t need to create self = this closures or use bind.