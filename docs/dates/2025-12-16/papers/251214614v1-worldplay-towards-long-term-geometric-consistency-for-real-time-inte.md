---
layout: default
title: WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling
---

# WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling
**arXiv**：[2512.14614v1](https://arxiv.org/abs/2512.14614) · [PDF](https://arxiv.org/pdf/2512.14614.pdf)  
**作者**：Wenqiang Sun, Haiyu Zhang, Haoyuan Wang, Junta Wu, Zehan Wang, Zhenwei Wang, Yunhong Wang, Jun Zhang, Tengfei Wang, Chunchao Guo  

**一句话要点**：提出WorldPlay流式视频扩散模型，实现实时交互式世界建模并保持长期几何一致性

**关键词**：流式视频扩散, 交互式世界建模, 长期几何一致性, 重构上下文记忆, 上下文强制蒸馏, 实时生成

## 3 点简述
- 核心问题：现有方法在速度与内存间存在权衡，难以实现实时交互式世界建模。
- 方法要点：采用双动作表示、重构上下文记忆和上下文强制蒸馏，确保长期几何一致性。
- 实验或效果：生成720p长视频达24 FPS，一致性优于现有技术，泛化性强。

## 摘要（原文）

> This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past frames and uses temporal reframing to keep geometrically important but long-past frames accessible, effectively alleviating memory attenuation. 3) We also propose Context Forcing, a novel distillation method designed for memory-aware model. Aligning memory context between the teacher and student preserves the student's capacity to use long-range information, enabling real-time speeds while preventing error drift. Taken together, WorldPlay generates long-horizon streaming 720p video at 24 FPS with superior consistency, comparing favorably with existing techniques and showing strong generalization across diverse scenes. Project page and online demo can be found: https://3d-models.hunyuan.tencent.com/world/ and https://3d.hunyuan.tencent.com/sceneTo3D.

