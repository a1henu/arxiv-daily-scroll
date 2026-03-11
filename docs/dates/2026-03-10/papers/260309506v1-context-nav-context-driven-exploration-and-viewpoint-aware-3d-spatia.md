---
layout: default
title: Context-Nav: Context-Driven Exploration and Viewpoint-Aware 3D Spatial Reasoning for Instance Navigation
---

# Context-Nav: Context-Driven Exploration and Viewpoint-Aware 3D Spatial Reasoning for Instance Navigation
**arXiv**：[2603.09506v1](https://arxiv.org/abs/2603.09506) · [PDF](https://arxiv.org/pdf/2603.09506.pdf)  
**作者**：Won Shik Jang, Ue-Hwan Kim  

**一句话要点**：提出Context-Nav，通过上下文驱动探索和视角感知3D空间推理解决文本目标实例导航问题。

**关键词**：文本目标实例导航, 上下文驱动探索, 视角感知3D空间推理, 密集文本-图像对齐, 价值图引导, 几何基础验证

## 3 点简述
- 核心问题：文本目标实例导航需在相同类别干扰物中定位特定实例，依赖长上下文描述。
- 方法要点：使用密集文本-图像对齐生成价值图引导探索，并基于视角感知3D空间关系验证候选目标。
- 实验或效果：无需任务特定训练，在InstanceNav和CoIN-Bench上达到最优性能，验证了方法的有效性。

## 摘要（原文）

> Text-goal instance navigation (TGIN) asks an agent to resolve a single, free-form description into actions that reach the correct object instance among same-category distractors. We present \textit{Context-Nav} that elevates long, contextual captions from a local matching cue to a global exploration prior and verifies candidates through 3D spatial reasoning. First, we compute dense text-image alignments for a value map that ranks frontiers -- guiding exploration toward regions consistent with the entire description rather than early detections. Second, upon observing a candidate, we perform a viewpoint-aware relation check: the agent samples plausible observer poses, aligns local frames, and accepts a target only if the spatial relations can be satisfied from at least one viewpoint. The pipeline requires no task-specific training or fine-tuning; we attain state-of-the-art performance on InstanceNav and CoIN-Bench. Ablations show that (i) encoding full captions into the value map avoids wasted motion and (ii) explicit, viewpoint-aware 3D verification prevents semantically plausible but incorrect stops. This suggests that geometry-grounded spatial reasoning is a scalable alternative to heavy policy training or human-in-the-loop interaction for fine-grained instance disambiguation in cluttered 3D scenes.

