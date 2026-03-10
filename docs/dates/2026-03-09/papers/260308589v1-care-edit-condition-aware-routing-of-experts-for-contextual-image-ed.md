---
layout: default
title: CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing
---

# CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing
**arXiv**：[2603.08589v1](https://arxiv.org/abs/2603.08589) · [PDF](https://arxiv.org/pdf/2603.08589.pdf)  
**作者**：Yucheng Wang, Zedong Wang, Yuetong Wu, Yue Ma, Dan Xu  

**一句话要点**：提出条件感知专家路由方法CARE-Edit，以解决多条件图像编辑中的任务干扰和冲突问题。

**关键词**：条件感知路由, 扩散模型, 多模态编辑, 专家网络, 图像编辑

## 3 点简述
- 核心问题：统一扩散编辑器在多样化任务中因固定共享骨干导致任务干扰，多条件输入下易产生颜色渗漏、身份漂移等伪影。
- 方法要点：通过轻量级潜在注意力路由器，基于多模态条件和扩散时间步动态分配计算给文本、掩码、参考和基础四个专家模块。
- 实验或效果：在擦除、替换、文本驱动编辑和风格迁移等任务上验证了性能，展示了动态条件感知处理对缓解多条件冲突的重要性。

## 摘要（原文）

> Unified diffusion editors often rely on a fixed, shared backbone for diverse tasks, suffering from task interference and poor adaptation to heterogeneous demands (e.g., local vs global, semantic vs photometric). In particular, prevalent ControlNet and OmniControl variants combine multiple conditioning signals (e.g., text, mask, reference) via static concatenation or additive adapters which cannot dynamically prioritize or suppress conflicting modalities, thus resulting in artifacts like color bleeding across mask boundaries, identity or style drift, and unpredictable behavior under multi-condition inputs. To address this, we propose Condition-Aware Routing of Experts (CARE-Edit) that aligns model computation with specific editing competencies. At its core, a lightweight latent-attention router assigns encoded diffusion tokens to four specialized experts--Text, Mask, Reference, and Base--based on multi-modal conditions and diffusion timesteps: (i) a Mask Repaint module first refines coarse user-defined masks for precise spatial guidance; (ii) the router applies sparse top-K selection to dynamically allocate computation to the most relevant experts; (iii) a Latent Mixture module subsequently fuses expert outputs, coherently integrating semantic, spatial, and stylistic information to the base images. Experiments validate CARE-Edit's strong performance on contextual editing tasks, including erasure, replacement, text-driven edits, and style transfer. Empirical analysis further reveals task-specific behavior of specialized experts, showcasing the importance of dynamic, condition-aware processing to mitigate multi-condition conflicts.

