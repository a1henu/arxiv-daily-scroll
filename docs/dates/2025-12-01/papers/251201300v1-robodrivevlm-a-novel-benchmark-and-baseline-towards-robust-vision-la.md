---
layout: default
title: RoboDriveVLM: A Novel Benchmark and Baseline towards Robust Vision-Language Models for Autonomous Driving
---

# RoboDriveVLM: A Novel Benchmark and Baseline towards Robust Vision-Language Models for Autonomous Driving
**arXiv**：[2512.01300v1](https://arxiv.org/abs/2512.01300) · [PDF](https://arxiv.org/pdf/2512.01300.pdf)  
**作者**：Dacheng Liao, Mengshi Qi, Peng Shu, Zhining Zhang, Yuxin Lin, Liang Liu, Huadong Ma  

**一句话要点**：提出RoboDriveVLM框架与RoboDriveBench基准，以增强自动驾驶中视觉语言模型的鲁棒性。

**关键词**：自动驾驶, 视觉语言模型, 鲁棒性基准, 多模态融合, 测试时适应, 轨迹预测

## 3 点简述
- 核心问题：现有VLM自动驾驶系统在真实场景中面临传感器和提示损坏等风险，鲁棒性不足。
- 方法要点：通过多模态数据映射和跨模态知识蒸馏的测试时适应方法，提升系统鲁棒性。
- 实验或效果：在包含11种模拟场景的基准上评估，提供更可靠的自动驾驶解决方案。

## 摘要（原文）

> Current Vision-Language Model (VLM)-based end-to-end autonomous driving systems often leverage large language models to generate driving decisions directly based on their understanding of the current scene. However, such systems introduce multiple risks in real-world driving scenarios. To evaluate whether VLMs are truly viable for autonomous driving, we introduce RoboDriveBench, the first robustness benchmark focused on end-to-end trajectory prediction tasks. This benchmark systematically evaluates two critical categories of real-world challenges for VLM-based end-to-end autonomous driving systems through 11 simulated scenarios encompassing various corruption types, including 6 scenarios of sensor corruption caused by environmental variations, along with 5 cases of prompt corruption resulting from human intervention and data transmission failures. Each corruption type includes 250 unique driving scenarios and 5,689 frames, resulting in 64,559 total trajectory prediction cases per evaluation. To overcome these real-world challenges, we propose a novel VLM-based autonomous driving framework called RoboDriveVLM, which enhances robustness by mapping more multimodal data-e.g., lidar and radar-into a unified latent space. Furthermore, we introduce a new Test-Time Adaptation (TTA) method based on cross-modal knowledge distillation to improve the robustness of VLM-based autonomous driving systems. Through extensive experiments, our work highlights the limitations of current VLM-based end-to-end autonomous driving systems and provides a more reliable solution for real-world deployment. Source code and datasets will be released.

