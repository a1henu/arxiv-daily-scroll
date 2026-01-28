---
layout: default
title: Fuzzy expert system for the process of collecting and purifying acidic water: a digital twin approach
---

# Fuzzy expert system for the process of collecting and purifying acidic water: a digital twin approach
**arXiv**：[2601.19527v1](https://arxiv.org/abs/2601.19527) · [PDF](https://arxiv.org/pdf/2601.19527.pdf)  
**作者**：Temirbolat Maratuly, Pakizar Shamoi, Timur Samigulin  

**一句话要点**：提出模糊专家系统结合数字孪生，用于酸性水收集与净化过程的自动化控制。

**关键词**：模糊专家系统, 数字孪生, 酸性水净化, 过程控制, 系统仿真

## 3 点简述
- 核心问题：酸性水含硫化氢等成分，未处理会污染环境并加速设备腐蚀。
- 方法要点：基于工业过程开发数字孪生，模糊控制器模拟人类推理，采用分程控制阀门。
- 实验或效果：测试105个场景，评估误差和动态响应指标，开发基于Python的Web仿真界面。

## 摘要（原文）

> Purifying sour water is essential for reducing emissions, minimizing corrosion risks, enabling the reuse of treated water in industrial or domestic applications, and ultimately lowering operational costs. Moreover, automating the purification process helps reduce the risk of worker harm by limiting human involvement. Crude oil contains acidic components such as hydrogen sulfide, carbon dioxide, and other chemical compounds. During processing, these substances are partially released into sour water. If not properly treated, sour water poses serious environmental threats and accelerates the corrosion of pipelines and equipment. This paper presents a fuzzy expert system, combined with a custom-generated digital twin, developed from a documented industrial process to maintain key parameters at desired levels by mimicking human reasoning. The control strategy is designed to be simple and intuitive, allowing junior or non-expert personnel to interact with the system effectively. The digital twin was developed using Honeywell UniSim Design R492 to simulate real industrial behavior accurately. Valve dynamics were modeled through system identification in MATLAB, and real-time data exchange between the simulator and controller was established using OPC DA. The fuzzy controller applies split-range control to two valves and was tested under 21 different initial pressure conditions using five distinct defuzzification strategies, resulting in a total of 105 unique test scenarios. System performance was evaluated using both error-based metrics (MSE, RMSE, MAE, IAE, ISE, ITAE) and dynamic response metrics, including overshoot, undershoot, rise time, fall time, settling time, and steady-state error. A web-based simulation interface was developed in Python using the Streamlit framework. Although demonstrated here for sour water treatment, the proposed fuzzy expert system is general-purpose.

