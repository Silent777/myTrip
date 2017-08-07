import React from "react";
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';

import {checkpointDetails, deleteUpadateList} from './actions/index.js'

class CheckpoinItem extends React.Component {
    constructor(props) {
        super(props);
        this.delete = this.delete.bind(this);
    }

    delete (event) {
        this.props.deleteCheckpoint(this.props.list.id)
    }

    render() {
        return (
            <div>
                <button className='checkpoint' onClick={() => this.props.checkpointDetails(this.props.checkpoint)}>
                    id:{this.props.checkpoint.id} - 
                    title: {this.props.checkpoint.title}
                </button>
                <span onClick={() => this.props.deleteUpadateList(this.props.checkpoint.id)}
                    className="glyphicon glyphicon-remove">
                </span>
            </div>
        );
    }
}

function matchDispatchToProps(dispatch){
    return bindActionCreators(
        {checkpointDetails: checkpointDetails,
        deleteUpadateList:deleteUpadateList},
        dispatch);
}

export default connect(null, matchDispatchToProps)(CheckpoinItem);