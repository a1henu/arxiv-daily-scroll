---
layout: default
title: DEFT-LLM: Disentangled Expert Feature Tuning for Micro-Expression Recognition
---

# DEFT-LLM: Disentangled Expert Feature Tuning for Micro-Expression Recognition
**arXiv**：[2511.10948v1](https://arxiv.org/abs/2511.10948) · [PDF](https://arxiv.org/pdf/2511.10948.pdf)  
**作者**：Ren Zhang, Huilai Li, Chao qi, Guoliang Xu, Tianyu Zhou, Wei wei, Jianqin Yin  

**一句话要点**：提出DEFT-LLM以解决微表情识别中的运动语义对齐问题

**关键词**：微表情识别, 多模态大语言模型, 运动语义对齐, 专家解耦, 指令数据集, 可解释建模

## 3 点简述
- 核心问题：静态外观与动态运动线索纠缠，文本标签与面部肌肉运动存在语义鸿沟。
- 方法要点：通过多专家解耦将面部动态分解为结构、动态纹理和运动语义表示。
- 实验或效果：在多个MER基准测试中实现最先进性能，提升局部面部运动的可解释建模。

## 摘要（原文）

> Micro expression recognition (MER) is crucial for inferring genuine emotion. Applying a multimodal large language model (MLLM) to this task enables spatio-temporal analysis of facial motion and provides interpretable descriptions. However, there are still two core challenges: (1) The entanglement of static appearance and dynamic motion cues prevents the model from focusing on subtle motion; (2) Textual labels in existing MER datasets do not fully correspond to underlying facial muscle movements, creating a semantic gap between text supervision and physical motion. To address these issues, we propose DEFT-LLM, which achieves motion semantic alignment by multi-expert disentanglement. We first introduce Uni-MER, a motion-driven instruction dataset designed to align text with local facial motion. Its construction leverages dual constraints from optical flow and Action Unit (AU) labels to ensure spatio-temporal consistency and reasonable correspondence to the movements. We then design an architecture with three experts to decouple facial dynamics into independent and interpretable representations (structure, dynamic textures, and motion-semantics). By integrating the instruction-aligned knowledge from Uni-MER into DEFT-LLM, our method injects effective physical priors for micro expressions while also leveraging the cross modal reasoning ability of large language models, thus enabling precise capture of subtle emotional cues. Experiments on multiple challenging MER benchmarks demonstrate state-of-the-art performance, as well as a particular advantage in interpretable modeling of local facial motion.

