import React from "react";
import { Link } from 'react-router-dom';

import AppBar from 'material-ui/AppBar';
import FlatButton from 'material-ui/FlatButton';

import { logged } from './utils';
import { logoutService } from './registration/registration.service';

const style = {
    LabelSize : {
        fontSize:"1.3em"
    },

    iconLeftStyle : {
         fontSize:"2em"
    },

    iconRightStyle : {
        marginBottom:"8px",
        display:"flex",
        alignItems:"center"
    }
}

export default class Header extends React.Component {
    constructor(props) {
        super(props);
    }

    logout = () => {
        logoutService()
            .then((response) => {
                this.props.loginHandler(false);
            })
            .catch((error) => console.dir(error));

    }

    render() {
        let elementRight;
        if (!logged()) {
            elementRight = (
                <div className='title'>
                    <FlatButton
                        className='header_btn'
                        label='REGISTRATION'
                        labelStyle={ style.LabelSize }
                        containerElement={<Link to="/registration"/>}
                    />
                    <FlatButton
                        className='header_btn'
                        label='LOGIN'
                        containerElement={<Link to="/login"/>}
                        labelStyle = {style.LabelSize}
                    />
                </div>
            )
        } else {
            elementRight =  (
                <div className='title'>
                    <FlatButton
                        label='LOGOUT'
                        className='header_btn'
                        onTouchTap = {this.logout}
                        labelStyle = { style.LabelSize }
                    />
                </div>
            )
        }
        return (
            <AppBar
                className='header'
                iconStyleLeft = { style.iconLeftStyle }
                iconElementLeft = {
                    <div className='title'>
                        <img className='header_icon' src='/static/src/img/logo.png' />
                        <Link to='/'>TripTracker</Link>
                    </div>
                }
                iconElementRight = { elementRight }
                iconStyleRight = { style.iconRightStyle }
            />
        );
    }
}
