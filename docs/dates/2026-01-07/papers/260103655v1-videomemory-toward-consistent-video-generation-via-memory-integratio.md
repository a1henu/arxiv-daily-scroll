---
layout: default
title: VideoMemory: Toward Consistent Video Generation via Memory Integration
---

# VideoMemory: Toward Consistent Video Generation via Memory Integration
**arXiv**：[2601.03655v1](https://arxiv.org/abs/2601.03655) · [PDF](https://arxiv.org/pdf/2601.03655.pdf)  
**作者**：Jinsong Zhou, Yihua Du, Xinli Xu, Luozhou Wang, Zijie Zhuang, Yehang Zhang, Shuaibo Li, Xiaojun Hu, Bolan Su, Ying-cong Chen  

**一句话要点**：提出VideoMemory框架，通过动态记忆库解决叙事视频生成中的实体一致性挑战。

**关键词**：视频生成, 实体一致性, 动态记忆库, 叙事规划, 多镜头基准

## 3 点简述
- 核心问题：现有模型在场景变化或长时间间隔后难以保持角色、道具和环境的身份与外观一致性。
- 方法要点：采用动态记忆库存储和更新实体的视觉与语义描述符，结合多智能体系统进行叙事分解和视频合成。
- 实验或效果：在54个多镜头一致性基准测试中，VideoMemory展现出强实体级连贯性和高感知质量。

## 摘要（原文）

> Maintaining consistent characters, props, and environments across multiple shots is a central challenge in narrative video generation. Existing models can produce high-quality short clips but often fail to preserve entity identity and appearance when scenes change or when entities reappear after long temporal gaps. We present VideoMemory, an entity-centric framework that integrates narrative planning with visual generation through a Dynamic Memory Bank. Given a structured script, a multi-agent system decomposes the narrative into shots, retrieves entity representations from memory, and synthesizes keyframes and videos conditioned on these retrieved states. The Dynamic Memory Bank stores explicit visual and semantic descriptors for characters, props, and backgrounds, and is updated after each shot to reflect story-driven changes while preserving identity. This retrieval-update mechanism enables consistent portrayal of entities across distant shots and supports coherent long-form generation. To evaluate this setting, we construct a 54-case multi-shot consistency benchmark covering character-, prop-, and background-persistent scenarios. Extensive experiments show that VideoMemory achieves strong entity-level coherence and high perceptual quality across diverse narrative sequences.

