---
layout: default
title: Prompt2Craft: Generating Functional Craft Assemblies with LLMs
---

# Prompt2Craft: Generating Functional Craft Assemblies with LLMs
**arXiv**：[2512.04568v1](https://arxiv.org/abs/2512.04568) · [PDF](https://arxiv.org/pdf/2512.04568.pdf)  
**作者**：Vitor Hideyo Isume, Takuya Kiyokawa, Natsuki Yamanobe, Yukiyasu Domae, Weiwei Wan, Kensuke Harada  

**一句话要点**：提出Prompt2Craft方法，利用LLMs生成功能性手工组装，解决机器人基于可用物体组装目标对象的任务。

**关键词**：机器人组装, 目标表示, 掩码分割, 模板检索, 形状简化, 比例匹配

## 3 点简述
- 核心问题：机器人如何从可用物体中选取子集，组装成目标对象的准确表示，物体不直接对应目标部件。
- 方法要点：使用掩码分割网络识别可见部分，检索模板网格，简化形状，设计搜索算法匹配局部和全局比例。
- 实验或效果：在两种场景中与基线方法结果相当，并在真实场景中展示定性结果。

## 摘要（原文）

> Inspired by traditional handmade crafts, where a person improvises assemblies based on the available objects, we formally introduce the Craft Assembly Task. It is a robotic assembly task that involves building an accurate representation of a given target object using the available objects, which do not directly correspond to its parts. In this work, we focus on selecting the subset of available objects for the final craft, when the given input is an RGB image of the target in the wild. We use a mask segmentation neural network to identify visible parts, followed by retrieving labeled template meshes. These meshes undergo pose optimization to determine the most suitable template. Then, we propose to simplify the parts of the transformed template mesh to primitive shapes like cuboids or cylinders. Finally, we design a search algorithm to find correspondences in the scene based on local and global proportions. We develop baselines for comparison that consider all possible combinations, and choose the highest scoring combination for common metrics used in foreground maps and mask accuracy. Our approach achieves comparable results to the baselines for two different scenes, and we show qualitative results for an implementation in a real-world scenario.

