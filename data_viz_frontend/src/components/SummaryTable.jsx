import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button } from '@mui/material';
import { useState,useEffect, useRef } from 'react';




function createData(id ,school_id, student_id , class_id , subject_id , aarea_id, answer_id,correct_ans_id, correct_ans
    ,syd_part, syd_perc, participant, cappc , award_id , year_level_name , student_score ) {
    return { id , school_id, student_id , class_id , subject_id , aarea_id, answer_id,correct_ans_id, correct_ans
        ,syd_part, syd_perc, participant, cappc , award_id , year_level_name , student_score};
  }
  let rows = [];

  export default function SummaryTable() {

    const [fetchedData, setFetchedData] = useState(0)
    const fromIndex = useRef({
      index: 0
    })
    const toIndex = useRef({
      index: 100
    })

    const fetchRows = () => 
    {

      let url = "http://127.0.0.1:8000/home/?category=summary&from=" + fromIndex.current.index + "&to=" + toIndex.current.index;
      fetch(url)
        .then(response => {
          console.log(url);

          return response.json();
        })
        .then(data => {
          // rows = []
          data.forEach(element => {
            rows.push(createData(element.pk , element.fields.school_id, element.fields.student_id,
              element.fields.class_id, element.fields.subject_id, element.fields.assessment_area_id,
              element.fields.answer_id, element.fields.correct_answer_id, element.fields.correct_answer
              ,element.fields.sydney_participants,element.fields.sydney_percentile,
              element.fields.participant,element.fields.correct_answer_percentage_per_class,
              element.fields.award_id,element.fields.year_level_name,element.fields.student_score))
            
          });
          fromIndex.current.index = toIndex.current.index;
          toIndex.current.index = toIndex.current.index + 100;
          console.log(fromIndex.current.index , toIndex.current.index)
          setFetchedData(toIndex.current.index)
        })
    }


    return (
      <div>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>School Id</TableCell>
              <TableCell align="right">Student Id</TableCell>
              <TableCell align="right">Class Id</TableCell>
              <TableCell align="right">Subject Id</TableCell>
              <TableCell align="right">Assessment Area Id</TableCell>
              <TableCell align="right">Answer Id</TableCell>
              <TableCell align="right">Correct Answer Id</TableCell>
              <TableCell align="right">Correct Answer</TableCell>
              <TableCell align="right">Sydney Participants</TableCell>
              <TableCell align="right">Sydney Percentile</TableCell>
              <TableCell align="right">Participant</TableCell>
              <TableCell align="right">Correct Answer Percentage per Class</TableCell>
              <TableCell align="right">Award Id</TableCell>
              <TableCell align="right">Year Level Name</TableCell>
              <TableCell align="right">Student Score</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row.id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.school_id}
                </TableCell>
                <TableCell align="right">{row.student_id}</TableCell>
                <TableCell align="right">{row.class_id}</TableCell>
                <TableCell align="right">{row.subject_id}</TableCell>
                <TableCell align="right">{row.aarea_id}</TableCell>
                <TableCell align="right">{row.answer_id}</TableCell>
                <TableCell align="right">{row.correct_ans_id}</TableCell>
                <TableCell align="right">{row.correct_ans}</TableCell>
                <TableCell align="right">{row.syd_part}</TableCell>
                <TableCell align="right">{row.syd_perc}</TableCell>
                <TableCell align="right">{row.participant}</TableCell>
                <TableCell align="right">{row.cappc}</TableCell>
                <TableCell align="right">{row.award_id}</TableCell>
                <TableCell align="right">{row.year_level_name}</TableCell>
                <TableCell align="right">{row.student_score}</TableCell>

              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
       <Button variant="text" fullWidth onClick={fetchRows}>Fetch Data</Button>
       </div>
    );

}