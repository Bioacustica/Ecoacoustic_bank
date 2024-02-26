import axios from "axios";
import React, { useState, useEffect } from "react";
import PublicFilter from "./PublicFilter";
function Filter_Public() {
  useEffect(() => {
    const fetchData = async () => {
      const { data } = await axios.get("192.168.0.2:3000/lista_filtros/");
    };

    fetchData();
  }, []);
}

function Table_Public() {
  useEffect(() => {
    const fetchDota = async () => {
      const { dato } = await axios.get("http://192.168.0.2:3000/public-records/");
    };

    fetchDota();
  }, []);
}

export default Filter_Public;
Table_Public;
