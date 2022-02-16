import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import {} from "./PrivateLabelTable"
import PrivateLabelTable from './PrivateLabelTable'






// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Tabla del Filtro de etiquetado',
  component: PrivateLabelTable,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Tabla_Filtro_Etiquetado = (args) => {
return <PrivateLabelTable />;
}