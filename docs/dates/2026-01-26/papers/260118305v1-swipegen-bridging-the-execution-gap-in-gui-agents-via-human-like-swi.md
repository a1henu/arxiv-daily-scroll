---
layout: default
title: SwipeGen: Bridging the Execution Gap in GUI Agents via Human-like Swipe Synthesis
---

# SwipeGen: Bridging the Execution Gap in GUI Agents via Human-like Swipe Synthesis
**arXiv**：[2601.18305v1](https://arxiv.org/abs/2601.18305) · [PDF](https://arxiv.org/pdf/2601.18305.pdf)  
**作者**：Xuan Wang, Siyuan Su, Quantong Fu, Yongxiang Hu, Yangfan Zhou  

**一句话要点**：提出SwipeGen以解决GUI代理中滑动交互执行不准确的问题

**关键词**：GUI代理, 滑动交互合成, 人机交互基准, 自动化GUI探索, 执行能力增强

## 3 点简述
- 核心问题：现有GUI代理的滑动交互策略过于简化，无法模拟人类行为，成为任务完成瓶颈。
- 方法要点：将人类滑动手势分解为可量化维度，通过GUI探索自动合成人类化滑动交互。
- 实验或效果：构建首个滑动执行基准，GUISwiper代理实现69.07%准确率，比基线提升214%。

## 摘要（原文）

> With the widespread adoption of Graphical User Interface (GUI) agents for automating GUI interaction tasks, substantial research focused on improving GUI perception to ground task instructions into concrete action steps. However, the step execution capability of these agents has gradually emerged as a new bottleneck for task completion. In particular, existing GUI agents often adopt overly simplified strategies for handling swipe interactions, preventing them from accurately replicating human-like behavior. To address this limitation, we decompose human swipe gestures into multiple quantifiable dimensions and propose an automated pipeline SwipeGen to synthesize human-like swipe interactions through GUI exploration. Based on this pipeline, we construct and release the first benchmark for evaluating the swipe execution capability of GUI agents. Furthermore, leveraging the synthesized data, we propose GUISwiper, a GUI agent with enhanced interaction execution capabilities. Experimental results demonstrate that GUISwiper achieves a swipe execution accuracy of 69.07%, representing a 214% improvement over existing VLM baselines.

