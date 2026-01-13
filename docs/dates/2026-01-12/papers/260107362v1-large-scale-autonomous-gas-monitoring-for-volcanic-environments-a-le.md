---
layout: default
title: Large-Scale Autonomous Gas Monitoring for Volcanic Environments: A Legged Robot on Mount Etna
---

# Large-Scale Autonomous Gas Monitoring for Volcanic Environments: A Legged Robot on Mount Etna
**arXiv**：[2601.07362v1](https://arxiv.org/abs/2601.07362) · [PDF](https://arxiv.org/pdf/2601.07362.pdf)  
**作者**：Julia Richter, Turcan Tuna, Manthan Patel, Takahiro Miki, Devon Higgins, James Fox, Cesar Cadena, Andres Diaz, Marco Hutter  

**一句话要点**：提出四足机器人系统以解决火山环境中自主气体监测的移动性挑战

**关键词**：四足机器人, 火山气体监测, 自主导航, 质谱仪系统, 崎岖地形移动

## 3 点简述
- 核心问题：火山地形崎岖，轮式系统难以可靠进行原位气体测量，阻碍了火山气体排放的准确监测。
- 方法要点：基于ANYmal四足机器人，集成四极杆质谱仪系统，采用模块化自主栈，包括任务规划、全局规划、定位和地形感知局部导航。
- 实验或效果：在埃特纳火山进行三次自主任务，自主率达93-100%，成功检测气体源；并在遥控任务中测量天然喷气孔，检测到二氧化硫和二氧化碳。

## 摘要（原文）

> Volcanic gas emissions are key precursors of eruptive activity. Yet, obtaining accurate near-surface measurements remains hazardous and logistically challenging, motivating the need for autonomous solutions. Limited mobility in rough volcanic terrain has prevented wheeled systems from performing reliable in situ gas measurements, reducing their usefulness as sensing platforms. We present a legged robotic system for autonomous volcanic gas analysis, utilizing the quadruped ANYmal, equipped with a quadrupole mass spectrometer system. Our modular autonomy stack integrates a mission planning interface, global planner, localization framework, and terrain-aware local navigation. We evaluated the system on Mount Etna across three autonomous missions in varied terrain, achieving successful gas-source detections with autonomy rates of 93-100%. In addition, we conducted a teleoperated mission in which the robot measured natural fumaroles, detecting sulfur dioxide and carbon dioxide. We discuss lessons learned from the gas-analysis and autonomy perspectives, emphasizing the need for adaptive sensing strategies, tighter integration of global and local planning, and improved hardware design.

