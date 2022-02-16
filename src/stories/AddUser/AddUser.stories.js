import React from 'react';
import AddUser from './AddUser';
import { CustomDocumentation} from "./documentacion"


// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Agregar usuarios',
  component: AddUser,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentation
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const  Modal_Agregar_Usuarios = (args) => {
return <AddUser />;
}