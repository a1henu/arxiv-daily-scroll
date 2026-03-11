---
layout: default
title: ENIGMA-360: An Ego-Exo Dataset for Human Behavior Understanding in Industrial Scenarios
---

# ENIGMA-360: An Ego-Exo Dataset for Human Behavior Understanding in Industrial Scenarios
**arXiv**：[2603.09741v1](https://arxiv.org/abs/2603.09741) · [PDF](https://arxiv.org/pdf/2603.09741.pdf)  
**作者**：Francesco Ragusa, Rosario Leonardi, Michele Mazzamuto, Daniele Di Mauro, Camillo Quattrocchi, Alessandro Passanisi, Irene D'Ambra, Antonino Furnari, Giovanni Maria Farinella  

**一句话要点**：提出ENIGMA-360数据集以解决工业场景中缺乏真实视角互补数据的问题。

**关键词**：工业场景数据集, 自我中心-外部中心视角, 人类行为理解, 时空标注, 动作分割, 人机交互检测

## 3 点简述
- 核心问题：缺乏真实工业场景的自我中心（ego）和外部中心（exo）视角互补数据集，阻碍人类行为理解系统发展。
- 方法要点：提供180个自我中心和180个外部中心视频，时间同步并标注时空信息，支持多任务研究。
- 实验或效果：基线实验展示现有方法在动作分割、关键步骤识别和交互检测任务上的局限性，强调新模型需求。

## 摘要（原文）

> Understanding human behavior from complementary egocentric (ego) and exocentric (exo) points of view enables the development of systems that can support workers in industrial environments and enhance their safety. However, progress in this area is hindered by the lack of datasets capturing both views in realistic industrial scenarios. To address this gap, we propose ENIGMA-360, a new ego-exo dataset acquired in a real industrial scenario. The dataset is composed of 180 egocentric and 180 exocentric procedural videos temporally synchronized offering complementary information of the same scene. The 360 videos have been labeled with temporal and spatial annotations, enabling the study of different aspects of human behavior in industrial domain. We provide baseline experiments for 3 foundational tasks for human behavior understanding: 1) Temporal Action Segmentation, 2) Keystep Recognition and 3) Egocentric Human-Object Interaction Detection, showing the limits of state-of-the-art approaches on this challenging scenario. These results highlight the need for new models capable of robust ego-exo understanding in real-world environments. We publicly release the dataset and its annotations at https://iplab.dmi.unict.it/ENIGMA-360.

