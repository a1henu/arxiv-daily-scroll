---
layout: default
title: GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models
---

# GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models
**arXiv**：[2603.09079v1](https://arxiv.org/abs/2603.09079) · [PDF](https://arxiv.org/pdf/2603.09079.pdf)  
**作者**：Md Selim Sarowar, Omer Tariq, Sungho Kim  

**一句话要点**：提出GST-VLA，通过结构化高斯空间令牌和3D深度感知思维链，提升视觉-语言-动作模型在3D任务中的性能。

**关键词**：3D高斯表示, 深度感知推理, 视觉-语言-动作模型, 结构化令牌, 动作解码, 几何注意力

## 3 点简述
- 核心问题：传统VLA模型使用2D图像块令牌，缺乏几何结构，限制了3D感知能力。
- 方法要点：引入高斯空间令牌化器，将深度和语义特征转换为3D高斯原语，并设计深度感知思维链进行结构化推理。
- 实验或效果：在LIBERO和SimplerEnv基准测试中，性能分别提升2.0%和5.4%，通过消融实验验证各组件贡献。

## 摘要（原文）

> VLA models encode visual observations as 2D patch tokens with no intrinsic geometric structure. We introduce GST-VLA with two contributions. First, the Gaussian Spatial Tokenizer (GST) converts frozen dense depth and frozen semantic patch features into $N_g{=}128$ anisotropic 3D Gaussian primitives, each parameterized by a metric residual mean $μ\in \mathbb{R}^3$, log-scale covariance $\log σ\in \mathbb{R}^3$, and learned opacity $α\in (0,1)$. The covariance eigenstructure encodes local surface orientation, and opacity provides per-primitive geometric confidence, both inaccessible from scalar depth. Spatial attention pooling with learned queries concentrates the fixed token budget on geometrically salient regions rather than distributing uniformly. Second, 3D Depth-Aware Chain-of-Thought (DA-CoT) reasoning supervises four structured intermediate spatial thoughts, covering 3D object grounding, grasp affordance contact geometry, pairwise metric distances, and coarse SE(3) waypoints, as explicit generation targets in the training loss. A cross-attention sublayer at every VLM transformer block provides direct access to the raw 256-primitive Gaussian field during DA-CoT generation. A 300M-parameter flow-matching action expert with mixture-of-experts feedforward sublayers decodes 7-DoF delta action chunks via conditional ODE integration, conditioned on both VLM hidden states and DA-CoT outputs through dual cross-attention. Trained with composite $\mathcal{L}_\mathrm{flow} + \mathcal{L}_\mathrm{CoT} + \mathcal{L}_\mathrm{depth}$ across three progressive stages, GST-VLA achieves 96.4% on LIBERO (+2.0%), and 80.2% on SimplerEnv (+5.4%). Ablations isolate the contribution of each GST component, each DA-CoT thought, and each training stage, confirming independent and synergistic gains concentrated on precision demanding tasks.

