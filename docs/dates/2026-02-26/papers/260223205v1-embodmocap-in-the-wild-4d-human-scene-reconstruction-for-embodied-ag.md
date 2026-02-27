---
layout: default
title: EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents
---

# EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents
**arXiv**：[2602.23205v1](https://arxiv.org/abs/2602.23205) · [PDF](https://arxiv.org/pdf/2602.23205.pdf)  
**作者**：Wenjia Wang, Liang Pan, Huaijin Pi, Yuke Lou, Xuqian Ren, Yifan Wu, Zhouyingcheng Liao, Lei Yang, Rishabh Dabral, Christian Theobalt, Taku Komura  

**一句话要点**：提出EmbodMocap以解决野外场景下人体与场景统一重建的数据采集难题

**关键词**：野外4D重建, 双视图校准, 度量尺度对齐, 具身AI数据, 人体场景交互, 机器人运动控制

## 3 点简述
- 现有系统依赖昂贵设备，限制野外大规模人体运动数据采集
- 使用双移动iPhone联合校准RGB-D序列，实现统一度量坐标下人体与场景重建
- 实验验证双视图优于单视图，并应用于三个具身AI任务

## 摘要（原文）

> Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iphone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

