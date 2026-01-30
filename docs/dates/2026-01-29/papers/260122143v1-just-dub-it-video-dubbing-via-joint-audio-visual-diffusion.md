---
layout: default
title: JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion
---

# JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion
**arXiv**：[2601.22143v1](https://arxiv.org/abs/2601.22143) · [PDF](https://arxiv.org/pdf/2601.22143.pdf)  
**作者**：Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef, Urska Jelercic, Ofir Bibi, Or Patashnik, Daniel Cohen-Or  

**一句话要点**：提出基于联合音频-视觉扩散模型的视频配音方法，通过轻量LoRA实现输入视频到多语言配音的转换。

**关键词**：视频配音, 音频-视觉扩散模型, LoRA微调, 多模态生成, 唇部同步

## 3 点简述
- 核心问题：现有视频配音方法依赖复杂任务特定流程，在真实场景中效果不佳。
- 方法要点：利用音频-视觉基础模型，通过LoRA条件化输入视频，联合生成翻译音频和同步面部运动。
- 实验或效果：通过自生成多语言视频训练，保持说话者身份和唇部同步，提升视觉保真度和鲁棒性。

## 摘要（原文）

> Audio-Visual Foundation Models, which are pretrained to jointly generate sound and visual content, have recently shown an unprecedented ability to model multi-modal generation and editing, opening new opportunities for downstream tasks. Among these tasks, video dubbing could greatly benefit from such priors, yet most existing solutions still rely on complex, task-specific pipelines that struggle in real-world settings. In this work, we introduce a single-model approach that adapts a foundational audio-video diffusion model for video-to-video dubbing via a lightweight LoRA. The LoRA enables the model to condition on an input audio-video while jointly generating translated audio and synchronized facial motion. To train this LoRA, we leverage the generative model itself to synthesize paired multilingual videos of the same speaker. Specifically, we generate multilingual videos with language switches within a single clip, and then inpaint the face and audio in each half to match the language of the other half. By leveraging the rich generative prior of the audio-visual model, our approach preserves speaker identity and lip synchronization while remaining robust to complex motion and real-world dynamics. We demonstrate that our approach produces high-quality dubbed videos with improved visual fidelity, lip synchronization, and robustness compared to existing dubbing pipelines.

