---
layout: default
title: Learning Situated Awareness in the Real World
---

# Learning Situated Awareness in the Real World
**arXiv**：[2602.16682v1](https://arxiv.org/abs/2602.16682) · [PDF](https://arxiv.org/pdf/2602.16682.pdf)  
**作者**：Chuhan Li, Ruilin Han, Joy Hsu, Yongyuan Liang, Rajiv Dhawan, Jiajun Wu, Ming-Hsuan Yang, Xin Eric Wang  

**一句话要点**：提出SAW-Bench基准以评估多模态基础模型在真实世界视频中的自我中心情境感知能力

**关键词**：情境感知, 自我中心视频理解, 多模态基准, 空间推理, 真实世界视频

## 3 点简述
- 核心问题：现有基准忽视观察者中心关系，如视角、姿态和运动，导致模型情境感知不足
- 方法要点：引入SAW-Bench，包含786个真实世界视频和2071个问答对，涵盖六项自我中心感知任务
- 实验或效果：评估显示最佳模型Gemini 3 Flash与人类性能差距达37.66%，模型常无法推断连贯相机几何

## 摘要（原文）

> A core aspect of human perception is situated awareness, the ability to relate ourselves to the surrounding physical environment and reason over possible actions in context. However, most existing benchmarks for multimodal foundation models (MFMs) emphasize environment-centric spatial relations (relations among objects in a scene), while largely overlooking observer-centric relationships that require reasoning relative to agent's viewpoint, pose, and motion. To bridge this gap, we introduce SAW-Bench (Situated Awareness in the Real World), a novel benchmark for evaluating egocentric situated awareness using real-world videos. SAW-Bench comprises 786 self-recorded videos captured with Ray-Ban Meta (Gen 2) smart glasses spanning diverse indoor and outdoor environments, and over 2,071 human-annotated question-answer pairs. It probes a model's observer-centric understanding with six different awareness tasks. Our comprehensive evaluation reveals a human-model performance gap of 37.66%, even with the best-performing MFM, Gemini 3 Flash. Beyond this gap, our in-depth analysis uncovers several notable findings; for example, while models can exploit partial geometric cues in egocentric videos, they often fail to infer a coherent camera geometry, leading to systematic spatial reasoning errors. We position SAW-Bench as a benchmark for situated spatial intelligence, moving beyond passive observation to understanding physically grounded, observer-centric dynamics.

