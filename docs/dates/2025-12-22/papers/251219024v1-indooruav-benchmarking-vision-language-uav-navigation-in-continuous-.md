---
layout: default
title: IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments
---

# IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments
**arXiv**：[2512.19024v1](https://arxiv.org/abs/2512.19024) · [PDF](https://arxiv.org/pdf/2512.19024.pdf)  
**作者**：Xu Liu, Yu Liu, Hanshuo Qiu, Yang Qirong, Zhouhui Lian  

**一句话要点**：提出IndoorUAV基准与方法，专注于室内无人机视觉语言导航的连续环境评估。

**关键词**：室内无人机导航, 视觉语言导航, 3D场景模拟, 长程规划, 短程规划, 任务分解

## 3 点简述
- 核心问题：现有视觉语言导航研究多关注地面机器人或室外无人机，室内无人机导航缺乏基准。
- 方法要点：基于Habitat模拟器构建多样3D室内场景，模拟无人机动态并自动化生成自然语言指令。
- 实验或效果：创建包含长程和短程子集的超过16,000条高质量轨迹，并设计新型导航模型。

## 摘要（原文）

> Vision-Language Navigation (VLN) enables agents to navigate in complex environments by following natural language instructions grounded in visual observations. Although most existing work has focused on ground-based robots or outdoor Unmanned Aerial Vehicles (UAVs), indoor UAV-based VLN remains underexplored, despite its relevance to real-world applications such as inspection, delivery, and search-and-rescue in confined spaces. To bridge this gap, we introduce \textbf{IndoorUAV}, a novel benchmark and method specifically tailored for VLN with indoor UAVs. We begin by curating over 1,000 diverse and structurally rich 3D indoor scenes from the Habitat simulator. Within these environments, we simulate realistic UAV flight dynamics to collect diverse 3D navigation trajectories manually, further enriched through data augmentation techniques. Furthermore, we design an automated annotation pipeline to generate natural language instructions of varying granularity for each trajectory. This process yields over 16,000 high-quality trajectories, comprising the \textbf{IndoorUAV-VLN} subset, which focuses on long-horizon VLN. To support short-horizon planning, we segment long trajectories into sub-trajectories by selecting semantically salient keyframes and regenerating concise instructions, forming the \textbf{IndoorUAV-VLA} subset. Finally, we introduce \textbf{IndoorUAV-Agent}, a novel navigation model designed for our benchmark, leveraging task decomposition and multimodal reasoning. We hope IndoorUAV serves as a valuable resource to advance research on vision-language embodied AI in the indoor aerial navigation domain.

