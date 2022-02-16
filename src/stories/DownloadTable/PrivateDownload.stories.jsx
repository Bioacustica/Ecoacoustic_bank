import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import PrivateDownloadTable from './PrivateDownloadTable';





// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Tabla de descarga',
  component: PrivateDownloadTable,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Tabla_descarga = (args) => {
return <PrivateDownloadTable />;
}