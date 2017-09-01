import React from 'react';
import { Link } from 'react-router-dom';

import {List, ListItem} from 'material-ui/List';
import { logged } from '../utils';
import AuthorIcon from 'material-ui/svg-icons/social/person';
import AllTripsIcon from 'material-ui/svg-icons/maps/map';
import MyTripsIcon from 'material-ui/svg-icons/maps/terrain';
import FollowersIcon from 'material-ui/svg-icons/maps/local-library';
import HelpIcon from 'material-ui/svg-icons/action/help-outline';
import HomeIcon from 'material-ui/svg-icons/action/home';
import Subscribe from "../subscribe/Subscribe";
import './trip.less'


export default class TripNavigation extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            open: false,
        };
    };

    handleOpen = () => {
        this.setState({open: true});
    };

    render() {
        return (
            <div>
                <List>
                    <ListItem
                        key='home'
                        className='buttonHome'
                        primaryText='Home'
                        leftIcon={<HomeIcon />}
                        containerElement={<Link to='/' />}
                    />

                    <ListItem
                        key='trips'
                        className='buttonAllTrips'
                        primaryText='All trips'
                        leftIcon={<AllTripsIcon />}
                        containerElement={<Link to='/trips' />}
                    />

                    {(logged()) ?
                    <ListItem
                        key='my_trips'
                        className='buttonMyTrips'
                        primaryText='My trips'
                        leftIcon={<MyTripsIcon />}
                        containerElement={<Link to='/my_trips' />}
                    /> : false}

                    <ListItem
                        key='profile'
                        className='buttonProfile'
                        primaryText='Author'
                        leftIcon={<AuthorIcon />}
                        containerElement={<Link to={`/profile/${this.props.userId}`} />}
                    />

                    <ListItem
                        key='followers'
                        className='buttonFollowers'
                        primaryText='Subscribers'
                        leftIcon={<FollowersIcon />}
                        onTouchTap={this.handleOpen}
                    />
                    <ListItem
                        key='help'
                        className='buttonHelp'
                        primaryText='Help'
                        leftIcon={<HelpIcon />}
                        containerElement={<Link to='/help' />}
                    />
                </List>
                <Subscribe
                    open={this.state.open}
                    tripId={this.props.tripId}
                />
            </div>
        );
    }
}
