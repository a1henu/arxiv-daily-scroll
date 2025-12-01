---
layout: default
title: SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot
---

# SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot
**arXiv**：[2511.23300v1](https://arxiv.org/abs/2511.23300) · [PDF](https://arxiv.org/pdf/2511.23300.pdf)  
**作者**：Yara Mahmoud, Jeffrin Sam, Nguyen Khang, Marcelino Fernando, Issatay Tokmurziyev, Miguel Altamirano Cabrera, Muhammad Haris Khan, Artem Lykov, Dzmitry Tsetserukou  

**一句话要点**：提出SafeHumanoid，结合VLM-RAG驱动人形机器人上身阻抗控制以提升人机交互安全性

**关键词**：人形机器人控制, 视觉语言模型, 检索增强生成, 阻抗控制, 人机交互安全, 第一人称视觉

## 3 点简述
- 核心问题：人机交互需机器人根据场景和人类接近度调节阻抗与速度以确保安全
- 方法要点：利用视觉语言模型和检索增强生成处理第一人称视觉，映射到关节级阻抗命令
- 实验或效果：在桌面操作任务中自适应刚度和速度，保持任务成功率并提高安全性

## 摘要（原文）

> Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

