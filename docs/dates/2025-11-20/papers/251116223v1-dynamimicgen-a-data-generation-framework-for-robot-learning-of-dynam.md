---
layout: default
title: DynaMimicGen: A Data Generation Framework for Robot Learning of Dynamic Tasks
---

# DynaMimicGen: A Data Generation Framework for Robot Learning of Dynamic Tasks
**arXiv**：[2511.16223v1](https://arxiv.org/abs/2511.16223) · [PDF](https://arxiv.org/pdf/2511.16223.pdf)  
**作者**：Vincenzo Pomponi, Paolo Franceschi, Stefano Baraldo, Loris Roveda, Oliver Avram, Luca Maria Gambardella, Anna Valente  

**一句话要点**：提出DynaMimicGen框架以解决动态环境中机器人学习数据不足问题

**关键词**：机器人学习, 动态任务, 数据生成, 模仿学习, 轨迹生成

## 3 点简述
- 核心问题：动态环境下机器人学习需大量数据，人工收集困难且不切实际
- 方法要点：基于少量演示，分割任务并使用动态运动基元生成适应动态变化的轨迹
- 实验或效果：在长时程和接触丰富任务中，训练代理在动态变化下表现优异

## 摘要（原文）

> Learning robust manipulation policies typically requires large and diverse datasets, the collection of which is time-consuming, labor-intensive, and often impractical for dynamic environments. In this work, we introduce DynaMimicGen (D-MG), a scalable dataset generation framework that enables policy training from minimal human supervision while uniquely supporting dynamic task settings. Given only a few human demonstrations, D-MG first segments the demonstrations into meaningful sub-tasks, then leverages Dynamic Movement Primitives (DMPs) to adapt and generalize the demonstrated behaviors to novel and dynamically changing environments. Improving prior methods that rely on static assumptions or simplistic trajectory interpolation, D-MG produces smooth, realistic, and task-consistent Cartesian trajectories that adapt in real time to changes in object poses, robot states, or scene geometry during task execution. Our method supports different scenarios - including scene layouts, object instances, and robot configurations - making it suitable for both static and highly dynamic manipulation tasks. We show that robot agents trained via imitation learning on D-MG-generated data achieve strong performance across long-horizon and contact-rich benchmarks, including tasks like cube stacking and placing mugs in drawers, even under unpredictable environment changes. By eliminating the need for extensive human demonstrations and enabling generalization in dynamic settings, D-MG offers a powerful and efficient alternative to manual data collection, paving the way toward scalable, autonomous robot learning.

