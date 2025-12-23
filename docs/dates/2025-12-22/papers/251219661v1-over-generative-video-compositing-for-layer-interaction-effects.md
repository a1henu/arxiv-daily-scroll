---
layout: default
title: Over++: Generative Video Compositing for Layer Interaction Effects
---

# Over++: Generative Video Compositing for Layer Interaction Effects
**arXiv**：[2512.19661v1](https://arxiv.org/abs/2512.19661) · [PDF](https://arxiv.org/pdf/2512.19661.pdf)  
**作者**：Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  

**一句话要点**：提出Over++框架以解决视频合成中环境交互效果生成的难题

**关键词**：视频合成, 环境交互效果, 生成模型, 文本驱动编辑, 无监督增强

## 3 点简述
- 核心问题：现有视频生成模型难以在添加环境交互效果时保持输入视频的完整性
- 方法要点：基于文本提示和输入视频层合成半透明环境效果，无需相机姿态或深度监督
- 实验或效果：在有限数据训练下，生成多样且真实的效果，优于现有基线

## 摘要（原文）

> In professional video compositing workflows, artists must manually create environmental interactions-such as shadows, reflections, dust, and splashes-between foreground subjects and background layers. Existing video generative models struggle to preserve the input video while adding such effects, and current video inpainting methods either require costly per-frame masks or yield implausible results. We introduce augmented compositing, a new task that synthesizes realistic, semi-transparent environmental effects conditioned on text prompts and input video layers, while preserving the original scene. To address this task, we present Over++, a video effect generation framework that makes no assumptions about camera pose, scene stationarity, or depth supervision. We construct a paired effect dataset tailored for this task and introduce an unpaired augmentation strategy that preserves text-driven editability. Our method also supports optional mask control and keyframe guidance without requiring dense annotations. Despite training on limited data, Over++ produces diverse and realistic environmental effects and outperforms existing baselines in both effect generation and scene preservation.

