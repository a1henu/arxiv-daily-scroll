---
layout: default
title: SSR: A Generic Framework for Text-Aided Map Compression for Localization
---

# SSR: A Generic Framework for Text-Aided Map Compression for Localization
**arXiv**：[2603.04272v1](https://arxiv.org/abs/2603.04272) · [PDF](https://arxiv.org/pdf/2603.04272.pdf)  
**作者**：Mohammad Omama, Po-han Li, Harsh Goel, Minkyu Choi, Behdad Chalaki, Vaishnav Tadiparthi, Hossein Nourkhiz Mahjoub, Ehsan Moradi Pari, Sandeep P. Chinchali  

**一句话要点**：提出文本增强压缩框架SSR，通过文本与图像特征互补，降低地图存储与传输成本，提升机器人定位效率。

**关键词**：地图压缩, 文本增强, 机器人定位, 多模态学习, 视觉地点识别, 自适应嵌入

## 3 点简述
- 核心问题：机器人地图规模增大导致存储、传输和查询成本过高，影响定位性能。
- 方法要点：利用文本作为可无损压缩的模态，结合轻量文本描述和小图像特征向量，通过SSR学习自适应图像嵌入捕获互补信息。
- 实验或效果：在多个数据集上验证，SSR压缩比优于基线2倍，支持室内外视觉地点识别和对象中心蒙特卡洛定位。

## 摘要（原文）

> Mapping is crucial in robotics for localization and downstream decision-making. As robots are deployed in ever-broader settings, the maps they rely on continue to increase in size. However, storing these maps indefinitely (cold storage), transferring them across networks, or sending localization queries to cloud-hosted maps imposes prohibitive memory and bandwidth costs. We propose a text-enhanced compression framework that reduces both memory and bandwidth footprints while retaining high-fidelity localization. The key idea is to treat text as an alternative modality: one that can be losslessly compressed with large language models. We propose leveraging lightweight text descriptions combined with very small image feature vectors, which capture "complementary information" as a compact representation for the mapping task. Building on this, our novel technique, Similarity Space Replication (SSR), learns an adaptive image embedding in one shot that captures only the information "complementary" to the text descriptions. We validate our compression framework on multiple downstream localization tasks, including Visual Place Recognition as well as object-centric Monte Carlo localization in both indoor and outdoor settings. SSR achieves 2 times better compression than competing baselines on state-of-the-art datasets, including TokyoVal, Pittsburgh30k, Replica, and KITTI.

