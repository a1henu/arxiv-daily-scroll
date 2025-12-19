---
layout: default
title: Factorized Video Generation: Decoupling Scene Construction and Temporal Synthesis in Text-to-Video Diffusion Models
---

# Factorized Video Generation: Decoupling Scene Construction and Temporal Synthesis in Text-to-Video Diffusion Models
**arXiv**：[2512.16371v1](https://arxiv.org/abs/2512.16371) · [PDF](https://arxiv.org/pdf/2512.16371.pdf)  
**作者**：Mariam Hassan, Bastien Van Delft, Wuyang Li, Alexandre Alahi  

**一句话要点**：提出因子化视频生成以解决文本到视频扩散模型在场景构建和时序合成中的耦合问题

**关键词**：文本到视频生成, 因子化生成, 场景构建, 时序合成, 锚定帧, 扩散模型

## 3 点简述
- 核心问题：现有模型因初始帧语义错误导致复杂场景和时序指令失败
- 方法要点：通过LLM推理、T2I合成锚定帧和视频模型时序合成三阶段解耦任务
- 实验或效果：在T2V CompBench和VBench2基准上实现新SOTA，采样步骤减少70%

## 摘要（原文）

> State-of-the-art Text-to-Video (T2V) diffusion models can generate visually impressive results, yet they still frequently fail to compose complex scenes or follow logical temporal instructions. In this paper, we argue that many errors, including apparent motion failures, originate from the model's inability to construct a semantically correct or logically consistent initial frame. We introduce Factorized Video Generation (FVG), a pipeline that decouples these tasks by decomposing the Text-to-Video generation into three specialized stages: (1) Reasoning, where a Large Language Model (LLM) rewrites the video prompt to describe only the initial scene, resolving temporal ambiguities; (2) Composition, where a Text-to-Image (T2I) model synthesizes a high-quality, compositionally-correct anchor frame from this new prompt; and (3) Temporal Synthesis, where a video model, finetuned to understand this anchor, focuses its entire capacity on animating the scene and following the prompt. Our decomposed approach sets a new state-of-the-art on the T2V CompBench benchmark and significantly improves all tested models on VBench2. Furthermore, we show that visual anchoring allows us to cut the number of sampling steps by 70% without any loss in performance, leading to a substantial speed-up in sampling. Factorized Video Generation offers a simple yet practical path toward more efficient, robust, and controllable video synthesis

