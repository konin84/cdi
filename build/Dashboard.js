import React from "react";
import NewSidebar from "../components/NewSidebar";
import DashboardData from "./DashboardData";

export default function Dashboard() {
  return (
    <section className="flex">
      {/* Side bar here */}
      <NewSidebar />

      {/* Main page here */}
      <DashboardData/>
  
    </section>
  );
}
