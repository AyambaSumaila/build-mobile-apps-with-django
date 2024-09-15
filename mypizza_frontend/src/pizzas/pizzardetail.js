import React, { Component } from 'react';

class PizzarDetail extends React.Component {

    render(){
        return (
            <div>
                <h2>Pizza Detail: {p.id}</h2>
                <h2>{p.pizzar}</h2>
                <h2>{p.city}</h2>


            </div>
        )
    }
}

export 