---
layout: default
title: CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation
---

# CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation
**arXiv**：[2603.08652v1](https://arxiv.org/abs/2603.08652) · [PDF](https://arxiv.org/pdf/2603.08652.pdf)  
**作者**：Haodong Li, Chunmei Qing, Huanyu Zhang, Dongzhi Jiang, Yihang Zou, Hongbo Peng, Dingming Li, Yuhong Dai, ZePeng Lin, Juanxi Tian, Yi Zhou, Siqi Dai, Jingwei Wu  

**一句话要点**：提出CoCo框架，将推理过程表示为可执行代码，以提升文本到图像生成的精确性和可控性。

**关键词**：文本到图像生成, 代码驱动推理, 结构化布局, 可执行规划, 多模态模型

## 3 点简述
- 现有基于思维链的文本到图像生成方法依赖抽象自然语言规划，缺乏复杂空间布局和结构化视觉元素的精确性。
- CoCo通过生成可执行代码指定场景结构布局，在沙盒环境中渲染确定性草稿图像，再通过细粒度编辑生成最终图像。
- 在StructT2IBench、OneIG-Bench和LongText-Bench上，CoCo相比直接生成分别提升68.83%、54.8%和41.23%，优于其他思维链增强方法。

## 摘要（原文）

> Recent advancements in Unified Multimodal Models (UMMs) have significantly advanced text-to-image (T2I) generation, particularly through the integration of Chain-of-Thought (CoT) reasoning. However, existing CoT-based T2I methods largely rely on abstract natural-language planning, which lacks the precision required for complex spatial layouts, structured visual elements, and dense textual content. In this work, we propose CoCo (Code-as-CoT), a code-driven reasoning framework that represents the reasoning process as executable code, enabling explicit and verifiable intermediate planning for image generation. Given a text prompt, CoCo first generates executable code that specifies the structural layout of the scene, which is then executed in a sandboxed environment to render a deterministic draft image. The model subsequently refines this draft through fine-grained image editing to produce the final high-fidelity result. To support this training paradigm, we construct CoCo-10K, a curated dataset containing structured draft-final image pairs designed to teach both structured draft construction and corrective visual refinement. Empirical evaluations on StructT2IBench, OneIG-Bench, and LongText-Bench show that CoCo achieves improvements of +68.83%, +54.8%, and +41.23% over direct generation, while also outperforming other generation methods empowered by CoT. These results demonstrate that executable code is an effective and reliable reasoning paradigm for precise, controllable, and structured text-to-image generation. The code is available at: https://github.com/micky-li-hd/CoCo

