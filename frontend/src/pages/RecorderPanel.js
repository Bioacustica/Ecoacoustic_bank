import React, { useEffect, useState } from "react";
import Head from "../components/Head";
import AdministratorNavbar from "../components/AdministratorNavbar";
import imgbanner from "../images/02.banner 1/imgBanner.jpg";
import Footer from "../components/Footer";
import RecorderTable from "../components/RecorderTable";
import { getHardwareList, getRecorderList } from "../services/recorder";
import AddRecorder from "../components/AddRecorder";

require("typeface-poppins");
require("typeface-rubik");

function RecorderPanel() {
  const userRole = localStorage.getItem("rolename");

  const [showModal, setShowModal] = useState(false);
  const [recorderList, setRecorderList] = useState([]);
  const [hardwareList, setHardwareList] = useState([]);

  const openModal = () => setShowModal(true);

  const closeModal = () => setShowModal(false);

  const getRecorders = async () => {
    try {
      const { data: hardwareData } = await getHardwareList()
      const { data } = await getRecorderList();
      const hardwareLIst = hardwareData.hardwares
      setHardwareList(hardwareLIst)
      setRecorderList(() => (data.recorders || []).map(record => ({ ...record, hardware: hardwareLIst.filter(hw => hw.id_hardware === record.id_hardware)?.[0]?.description })));
    } catch (error) {}
  };

  const addRecorderList = (recorder) => {
    console.log({recorder})
    setRecorderList((recorders) => [...recorders, { ...recorder, hardware: hardwareList.filter(hw => hw.id_hardware === Number(recorder.id_hardware))?.[0]?.description }]);
  };

  const updateRecorderList = (recorder) => {
    console.log({recorder, hardware: hardwareList.filter(hw => hw.id_hardware === Number(recorder.id_hardware))?.[0]?.description})
    setRecorderList((recorders) =>
      (recorders || []).map((r) => (r.id_h_serial !== recorder.id_h_serial ? r : { ...recorder, hardware: hardwareList.filter(hw => hw.id_hardware === Number(recorder.id_hardware))?.[0]?.description }))
    );
  };

  useEffect(() => {
    getRecorders();
  }, []);

  return (
    <>
      <header className="sticky top-0 z-30 bg-white">
        <Head />
        <AdministratorNavbar />
      </header>

      <main>
        <div className="flex items-center justify-center">
          <div>
            <img src={imgbanner} alt="" />
          </div>
          <div className="absolute self-center justify-center ">
            <div className="space-y-3">
              <h1 className="text-center font-extrabold font-poppins text-4.5xl text-white">
                {userRole},
              </h1>
              <h1 className="text-center font-extrabold font-poppins  text-4.5xl text-white">
                Recorders
              </h1>
            </div>
          </div>
        </div>

        <div className="flex items-center justify-center mt-5 mb-3 ">
          <button
            onClick={openModal}
            className="w-87.75 bg-blue-250 text-white h-10.75 font-semibold text-2xl font-poppins"
          >
            Add recorder
          </button>
        </div>

        <div className="h-full">
          <RecorderTable recorderList={recorderList} updateRecorderList={updateRecorderList} hardwareList={hardwareList} />
        </div>

        {showModal && (
          <AddRecorder
            className="z-50"
            close={closeModal}
            addRecorderList={addRecorderList}
            hardwareList={hardwareList}
          />
        )}
      </main>

      <Footer />
    </>
  );
}

export default RecorderPanel;
