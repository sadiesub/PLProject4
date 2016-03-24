/**
 * Created by Levi on 3/19/2016.
 */

"use strict";

var list = function() {
    var list = function () {
        function Node(data) {
            this.data = data;
            this.next = null;
        }

        var l = {
            length: 0,
            currentNode: null,
            head: new Node(null),
            add: function(e) {
                if (l.currentNode === null) { // This is true the first time
                    l.head.data = e;
                    l.currentNode = new Node(null);
                    l.head.next = l.currentNode;
                    l.length++;
                }
                else {
                    l.currentNode.data = e;
                    var node = new Node(null);
                    l.currentNode.next = node;
                    l.currentNode = node;
                    l.length++;
                }
            },
        };

        var iterate = {

        }

        var F = function () {
        };
        var f = new F();

        // public data
        f.run = function (e) {
            return l[e];
        };
        f.first = f.car = function () {
            return l.head.data
        };
        f.rest = f.cdr = function () {
            if(l.length > 0) {
                l.head = l.head.next;
                l.length--;
            }
            return this;
        }
        f.concat = f.cons = function(e){
            if (typeof e === 'string' || e instanceof String) {l.add(e);}
            else {
                var n = e.run('head');
                for(var i = 0; i < e.run('length'); i++) {
                    l.add(n.data);
                    n = n.next;
                }
            }
        }
        f.length = function(){return l.length};
        f.map = function(f){
            if (f instanceof Function) {
                var n = l.head;
                for(var i = 0; i < l.length; i++) {
                    n.data = f(n.data);
                    n = n.next;
                }
            }
        }
        f.iterate = (function(){
            var n = l.head;
            var counter = 0;
            return function(){
                if(counter < 1){
                    counter += 1;
                    return n.data;
                }else{
                    counter += 1;
                    n = n.next;
                    return n.data;
                }
            }
        })();

        return f;
    }();
    return list;
};

var l1 = new list();
l1.concat('a')
l1.cons('b')
l1.concat('c')
l1.concat('d')
l1.concat('e')
l1.concat('f')


document.writeln("The following lines contain strings of the data" +
    "<br>" + " given by the function reference." + "<br>" +
"The list is ['a', 'b', 'c', 'd', 'e', 'f'].")
document.writeln("<br>1: " + l1.iterate());
document.writeln("<br>2: " + l1.iterate());
document.writeln("<br>3: " + l1.iterate());
document.writeln("<br>4: " + l1.iterate());
document.writeln("<br>5: " + l1.iterate());
document.writeln("<br>6: " + l1.iterate());