import React, { Component } from 'react';
import Calendar from 'react-calendar';
import './Calender.css';
import './App.css'
import allDates from './all_dates'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

 
class App extends Component {

  constructor(props){
    super(props)
    this.datesSet = new Set()
    for(let i = 0;i<allDates.length;++i){
      this.datesSet.add(allDates[i])
    }
  }

  state = {
    date: new Date(2016,10,15),
  }
 
  onChange = date => this.setState({ date })

  onClickGotoData(){
    let dateStr = dateToString(this.state.date)
    let newUrl = "/pages/dates/"+dateStr+".html"
    window.location.href = newUrl;
  }

  onClickAllPics(){
    alert("to be added")
  }

  onClickSearch(){
    alert("to be added")
  }

  dateIsDisabled(date){
    let dateStr = dateToString(date)
    let result = !this.datesSet.has(dateStr)
    //console.log("calling date is disabled "+dateStr+"   and the answer is "+result)
    return result
  }
 
  render() {
    return (
      <div>
        <div class="calender-div">
          <Calendar
            defaultActiveStartDate = {new Date(2016,10,15)}
            onChange={this.onChange}
            value={this.state.date}
            tileDisabled = { ({activeStartDate, date, view}) => {return this.dateIsDisabled(date)}}
          />
        </div>
        <div class="goto-date">
          <button onClick={()=>{this.onClickGotoData()}} disabled = {this.dateIsDisabled(this.state.date)}>
            前往日期
          </button>
        </div>
        <div class="all-pics">
          <button onClick={()=>{this.onClickAllPics()}}>
            相册
          </button>
        </div>
        <div class="search">
          <button onClick={()=>{this.onClickSearch()}}>
            搜索
          </button>
        </div>
      </div>
      
    );
  }
}


class Search extends Component {
  render(){
    return <p>haha</p>
  }
}





const dateToString = (date) =>{
  return date.toISOString().substring(0, 10).replace("-","_").replace("-","_");
}
export default App;