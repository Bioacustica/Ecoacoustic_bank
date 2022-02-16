import React from 'react';
import { CustomDocumentation} from "./documentacion"
import EditModal from './EditModal';


// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Editar audio',
  component: EditModal,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentation
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const  Modal_Editar_Audios = (args) => {
return <EditModal />;
}